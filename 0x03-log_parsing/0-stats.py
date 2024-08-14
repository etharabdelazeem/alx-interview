#!/usr/bin/python3
import sys
import signal


# Initialize metrics
total_file_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}


def print_stats():
    """Prints the computed metrics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def process_line(line):
    """Processes a single line to update the metrics"""
    global total_file_size

    try:
        parts = line.split()
        if len(parts) < 7:
            return  # skip line if it's malformed

        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update total file size
        total_file_size += file_size

        # Update the status code count if it's a known code
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

    except (ValueError, IndexError):
        # If there are any issues parsing the line, skip it
        return


def signal_handler(sig, frame):
    """Handles the KeyboardInterrupt signal to print the statistics"""
    print_stats()
    sys.exit(0)

    # Bind the signal handler for keyboard interrupt (CTRL + C)
    signal.signal(signal.SIGINT, signal_handler)

    line_count = 0

    # Read from stdin line by line
    for line in sys.stdin:
        process_line(line.strip())
        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

    # Print stats at the end if there are remaining lines
    print_stats()
