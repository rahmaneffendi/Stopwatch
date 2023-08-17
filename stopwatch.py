import time

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    print("Stopwatch started.")

    try:
        while True:
            elapsed_time = time.time() - start_time
            mins, secs = divmod(elapsed_time, 60)
            hours, mins = divmod(mins, 60)
            time_format = "{:02}:{:02}:{:05.2f}".format(int(hours), int(mins), secs)
            print(time_format, end='\r')
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nStopwatch stopped.")
        end_time = time.time()
        total_time = end_time - start_time
        print("Total time elapsed: {:.2f} seconds".format(total_time))

if __name__ == "__main__":
    stopwatch()
