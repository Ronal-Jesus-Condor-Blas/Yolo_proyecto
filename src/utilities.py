def calculate_times(detections):
    """
    Calcula el tiempo total que la puerta estuvo abierta o cerrada.
    """
    open_time = 0
    closed_time = 0
    last_state = None
    last_time = None

    for detection in detections:
        state, timestamp = detection["state"], detection["timestamp"]

        if last_state is not None and last_state != state:
            duration = timestamp - last_time
            if last_state == "abierta":
                open_time += duration
            elif last_state == "cerrada":
                closed_time += duration

        last_state = state
        last_time = timestamp

    return {"open_time": open_time, "closed_time": closed_time}

def save_results(results, filepath):
    """
    Guarda los resultados en un archivo.
    """
    with open(filepath, "w") as f:
        f.write(f"Tiempo abierta: {results['open_time']} segundos\n")
        f.write(f"Tiempo cerrada: {results['closed_time']} segundos\n")
    print(f"Resultados guardados en {filepath}.")
