months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    while True:
        try:
            date = input("Date: ").strip()

            # Case 1: Format like "September 8, 1636"
            if "," in date:
                month_str, day_year = date.split(" ", 1)
                day_str, year = day_year.replace(",", "").split()
                month = months.index(month_str.title()) + 1
                day = int(day_str)
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break

            # Case 2: Format like "9/8/1636"
            elif "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break

        except (ValueError, IndexError):
            # Invalid format — ask again
            continue

        except (EOFError, KeyboardInterrupt):
            print()
            break


main()
