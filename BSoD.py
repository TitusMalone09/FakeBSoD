import pygame
import os
import threading

class FullScreenApp:
    def __init__(self, img_folder):
        self.img_folder = img_folder
        self.img_files = ["Pre1.png", "Pre2.png"] + [f"{i*10}.png" for i in range(11)] + ["100.png"]
        self.running = True

        pygame.init()
        screen_info = pygame.display.Info()
        self.screen_width, self.screen_height = screen_info.current_w, screen_info.current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)

        pygame.mouse.set_visible(False)

        pygame.mixer.init()
        self.restart_timer = threading.Timer(29, self.restart_system)
        self.restart_timer.start()

        self.start_slideshow()

    def start_slideshow(self):
        clock = pygame.time.Clock()

        for img_file in self.img_files:
            if not self.running:
                break

            img_path = os.path.join(self.img_folder, img_file)
            img = pygame.image.load(img_path)
            img = pygame.transform.scale(img, (self.screen_width, self.screen_height))

            self.screen.blit(img, (0, 0))
            pygame.display.flip()

            delay = 100 if img_file in ["Pre1.png", "Pre2.png"] else 2000

            start_time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - start_time < delay:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.mod & pygame.KMOD_CTRL:
                        if event.key in [pygame.K_q, pygame.K_w, pygame.K_e]:
                            self.exit_fullscreen()
                            return
                clock.tick(30)

    def restart_system(self):
        os.system("shutdown /r /f /t 0")

    def exit_fullscreen(self):
        self.running = False
        self.restart_timer.cancel()
        pygame.quit()
        os._exit(0)

if __name__ == "__main__":
    img_folder = "C:/Users/user/Desktop/Pictures/BSoD"
    app = FullScreenApp(img_folder)