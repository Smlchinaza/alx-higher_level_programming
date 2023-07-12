import sys

def print_statistics(total_size, status_codes):
    """Print the accumulated statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

total_size = 0
status_codes = {}

try:
    for i, line in enumerate(sys.stdin, 1):
        # Split the line into its components
        ip, _, _, _, status_code, file_size = line.split()[0:6]

        # Update the total file size
        total_size += int(file_size)

        # Update the status code count
        status_codes[status_code] = status_codes.get(status_code, 0) + 1

        # Print statistics after every 10 lines
        if i % 10 == 0:
            print_statistics(total_size, status_codes)

except KeyboardInterrupt:
    # Handle keyboard interruption and print the final statistics
    print_statistics(total_size, status_codes)
