import cv2
from ffpyplayer.player import MediaPlayer
import requests
from audioDisplay import remove_downloaded_mp3
import time

# This class will be used to help support with video display with audio in the main driver
class AudioVideoDisplay:
    def __init__(self, videoLink: str):
        self.videoLink = videoLink
        self.video = cv2.VideoCapture(videoLink)
        self.player = MediaPlayer(videoLink)
    
    def displayAudioVideo(self):
        cap = cv2.VideoCapture(self.videoLink)
        cv2.namedWindow('Frame', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        r = requests.get(self.videoLink)
        with open("audio.mp3", "wb") as f:
            f.write(r.content)

        file = "./audio.mp3"
        
        start_time = time.time()
        while True:
            ret, frame = self.video.read()
            _, val = self.player.get_frame()

            if not ret:
                break

            # Get current video timestamp (assuming video timestamps are available)
            video_timestamp = self.video.get(cv2.CAP_PROP_POS_MSEC)

            # Calculate elapsed time since video start
            elapsed_time = (time.time() - start_time) * 1000  # msec

            # Adjust delay based on video and audio timestamps (heuristic approach)
            delay = max(1, int(video_timestamp - elapsed_time))

            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

            # Only display frame if audio is not finished
            if val != 'eof':
                cv2.imshow('Frame', frame)

        self.player.close_player()
        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)

        remove_downloaded_mp3(file)
        
# Example usage
def playAudioVideoFunction(mediaURL: str):        
    inputVideo = mediaURL
    video = AudioVideoDisplay(inputVideo)
    video.displayAudioVideo()