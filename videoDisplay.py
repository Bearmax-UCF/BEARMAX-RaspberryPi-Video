import cv2

# This class will be used to help support with video display in the main driver

class VideoDisplay:
    def __init__(self, videoLink: str):
        self.videoLink = videoLink
        self.video = cv2.VideoCapture(videoLink)
    def displayVideo(self) -> bool:
        cap = cv2.VideoCapture(self.videoLink)
        cv2.namedWindow('Frame', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        while cap.isOpened():
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow('Frame', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    return False
            else:
                return False
        cap.release()
        cv2.destroyAllWindows()
        return True

# Example usage
def main():        
    inputVideo= input("Enter the video link: ")
    video = VideoDisplay(inputVideo)
    video.displayVideo()

main()