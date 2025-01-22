from src.video_analysis import analyze_video
from src.live_analysis import analyze_live
from config import CONFIG

def main():
    print("Bienvenido al sistema de análisis de puerta.")
    mode = input("¿Qué deseas hacer? (video/vivo): ").strip().lower()

    if mode == "video":
        print("\nVideos disponibles para analizar:")
        for i, video_name in enumerate(CONFIG["VIDEOS"]):
            print(f"{i + 1}. {video_name}")

        choice = int(input("\nSelecciona el número del video a analizar: ")) - 1
        if 0 <= choice < len(CONFIG["VIDEOS"]):
            analyze_video(CONFIG["VIDEOS"][choice])
        else:
            print("Selección inválida.")
    elif mode == "vivo":
        analyze_live()
    else:
        print("Opción no válida. Por favor, elige 'video' o 'vivo'.")

if __name__ == "__main__":
    main()
