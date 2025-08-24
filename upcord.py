# Python v3.6+
# UpCord - CLI tool untuk mengunduh installer Discord terbaru secara otomatis,
#          mendukung Windows, macOS, dan Linux. Tidak membutuhkan library eksternal.
# GITHUB: https://github.com/denoyey/UpCord-CLI

import os, sys, random, urllib.request, platform, re

colors = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "MAGENTA": "\033[95m",
    "CYAN": "\033[96m",
    "WHITE": "\033[97m",
    "RESET": "\033[0m",
}


def clear_screen():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception as e:
        print(f"\n{colors['RED']}Error clearing screen: {e}{colors['RESET']}")


def logo():
    try:
        available_colors = [c for k, c in colors.items() if k != "RESET"]
        ascii_logo = r"""
▗▖ ▗▖▗▄▄▖  ▗▄▄▖ ▗▄▖ ▗▄▄▖ ▗▄▄▄       ▗▄▄▖ ▗▖   ▗▄▄▄▖
▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌  █      ▐▌   ▐▌     █  
▐▌ ▐▌▐▛▀▘ ▐▌   ▐▌ ▐▌▐▛▀▚▖▐▌  █ ▗▄▄▄▖▐▌   ▐▌     █  
▝▚▄▞▘▐▌   ▝▚▄▄▖▝▚▄▞▘▐▌ ▐▌▐▙▄▄▀      ▝▚▄▄▖▐▙▄▄▖▗▄█▄▖

 A CLI tool to download the latest Discord client
   GITHUB: https://github.com/denoyey/UpCord-CLI
    """
        for line in ascii_logo.strip("\n").split("\n"):
            print(f"{random.choice(available_colors)}{line}{colors['RESET']}")
    except Exception as e:
        print(f"\n{colors['RED']}Error displaying logo: {e}{colors['RESET']}")


def download_latest_discord(target_folder):
    try:
        sys_map = {
            "Windows": (
                "https://discord.com/api/download/stable?platform=win",
                "DiscordSetup.exe",
            ),
            "Darwin": (
                "https://discord.com/api/download/stable?platform=osx",
                "Discord.dmg",
            ),
            "Linux": (
                "https://discord.com/api/download/stable?platform=linux&format=deb",
                "discord.deb",
            ),
        }
        user_agents = {
            "Windows": [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
            ],
            "Darwin": [
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1)",
            ],
            "Linux": [
                "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0)",
                "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:85.0)",
            ],
        }
        system = platform.system()
        if system not in sys_map:
            print(f"{colors['RED']}Unsupported OS.{colors['RESET']}")
            return None
        base_url, default_filename = sys_map[system]
        user_agent = random.choice(user_agents.get(system, ["Mozilla/5.0"]))
        req = urllib.request.Request(base_url, headers={"User-Agent": user_agent})
        with urllib.request.urlopen(req) as response:
            final_url = response.geturl()
        version = re.search(r"/([\d\.]+)/", final_url)
        version = version.group(1) if version else "latest"
        filename = f"discord_{version}{os.path.splitext(default_filename)[1]}"
        output_path = os.path.join(target_folder, filename)
        if os.path.exists(output_path):
            print(
                f"{colors['YELLOW']}File {filename} already exists in {target_folder}.{colors['RESET']}"
            )
            decision = input(f"\nDo you want to redownload it? (y/N): ").strip().lower()
            if decision != "y":
                print(
                    f"\n{colors['CYAN']}Skipped downloading. Using existing file.{colors['RESET']}"
                )
                return output_path
            else:
                os.remove(output_path)
                print(
                    f"\n{colors['RED']}Old file deleted. Redownloading...{colors['RESET']}"
                )
        print(
            f"{colors['GREEN']}Downloading Discord {version} from:{colors['RESET']} {final_url}"
        )
        os.makedirs(target_folder, exist_ok=True)
        req_final = urllib.request.Request(
            final_url, headers={"User-Agent": user_agent}
        )
        with urllib.request.urlopen(req_final) as response:
            total = int(response.getheader("Content-Length") or 0)
            with open(output_path, "wb") as out:
                downloaded = 0
                while chunk := response.read(8192):
                    out.write(chunk)
                    downloaded += len(chunk)
                    if total:
                        percent = downloaded * 100 / total
                        bar = (
                            f"{'█' * int(percent // 2)}{'-' * (50 - int(percent // 2))}"
                        )
                        print(
                            f"\r[{bar}] {percent:.2f}% ({downloaded}/{total} bytes)",
                            end="",
                            flush=True,
                        )
        print(f"\n\n{colors['GREEN']}Saved to:{colors['RESET']} {output_path}")
        return output_path
    except Exception as e:
        print(f"\n{colors['RED']}Error: {e}{colors['RESET']}")
        return None


def main():
    try:
        while True:
            clear_screen()
            logo()
            print(
                f"{colors['WHITE']}[1] Download Discord (Latest Version)\n[0] Exit{colors['RESET']}"
            )
            choice = input(f"\n{colors['YELLOW']}>> {colors['RESET']}").strip()
            if choice == "1":
                clear_screen()
                logo()
                folder = "output_upcord"
                if download_latest_discord(folder):
                    print(
                        f"\n{colors['GREEN']}Download completed successfully!{colors['RESET']}"
                    )
                else:
                    print(f"\n{colors['RED']}Download failed.{colors['RESET']}")
                input(
                    f"\n{colors['CYAN']}Press Enter to return to menu...{colors['RESET']}"
                )
            elif choice == "0":
                clear_screen()
                logo()
                print(
                    f"{colors['YELLOW']}Thank you for using this tool :D{colors['RESET']}"
                )
                sys.exit(0)
            else:
                print(
                    f"\n{colors['RED']}Invalid choice, please try again.{colors['RESET']}"
                )
                input("\nPress Enter to continue...")
    except KeyboardInterrupt:
        print(f"\n\n{colors['YELLOW']}Exiting...{colors['RESET']}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{colors['RED']}An error occurred: {e}{colors['RESET']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
