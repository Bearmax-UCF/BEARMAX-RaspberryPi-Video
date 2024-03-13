import cv2

# This class will be used to help support with video display in the main driver

class VideoDisplay:
    def __init__(self, videoLink: str):
        self.videoLink = videoLink
        self.video = cv2.VideoCapture(videoLink)
    def displayVideo(self):
        cap = cv2.VideoCapture(self.videoLink)
        cv2.namedWindow('Frame', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        while cap.isOpened():
            ret, frame = cap.read()
            
            if ret:
                cv2.imshow('Frame', frame)

            else:
                break

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)
test="https://bearmaxtest.blob.core.windows.net/test/Metal_pipe_falling_sound_effectloud.mp4?sp=r&st=2024-03-13T05:10:29Z&se=2024-03-13T13:10:29Z&spr=https&sv=2022-11-02&sr=b&sig=V9rSsSetFc%2BhirlWk8CjJu8KpAgQZDCN%2BJGUMEpzkEU%3D"
# Example usage
def main():        
    inputVideo= input("Enter the video link: ")
    video = VideoDisplay(inputVideo)
    video.displayVideo()
main()