# PC Guy

> A Windows system optimization toolkit by the [samai.cc](https://samai.cc) group.

PC Guy is a Windows desktop utility written in Go, with a web-based management panel and a system tray icon, helping you easily optimize and maintain your Windows PC.

## Features

- **Memory Cleanup**: Scan memory usage and free up memory by clearing working sets of processes with one click.
- **CPU Monitor**: View CPU usage, core count, temperature (temperature may be unavailable on some devices), and process count.
- **Process Manager**: List all processes with CPU/memory usage, sort by usage, and terminate suspicious or high-usage processes (with auto-refresh).
- **Junk Cleaner**: Scan and clean system temp files, Recycle Bin, browser caches, Windows logs, prefetch, and recent documents.
- **Software Manager**: List installed software and uninstall with one click.
- **Startup Manager**: View / enable / disable / delete startup items (registry Run keys and Startup folder).
- **Force Delete**: Recursively force-delete folders (ignoring read-only / hidden attributes).
- **Agent Takeover**: Bundles the `samcommand` service. Temporarily enable "Takeover Mode" so another AI agent can execute commands remotely via a public URL to help fix issues; the panel shows the public address and auth token — turn it off when done.
- **System Tray**: Right-click menu with mutually exclusive "Run at startup / Cancel startup", "Enable / Disable takeover mode", "Management panel", and "Exit".

## Download & Install

Go to the [Releases](https://github.com/samaidev/pcguy_r/releases) page and download the latest `PCGuy-setup-x.x.x.exe` installer. Double-click to install; shortcuts are created on the desktop and in the Start menu.

## Usage

After launch, the PC Guy icon appears in the system tray. Right-click to open the management panel or exit.

The UI defaults to English and also supports Chinese. Switch via the button at the top-right of the panel or a launch argument:

```bash
pcguy.exe            # English (default)
pcguy.exe --lang zh # Chinese
```

## About samai.cc

samai.cc is a group focused on AI and system-tool development, dedicated to helping users get more out of their computers through intelligent solutions. Learn more at <https://samai.cc>.

## License

This repository is for product introduction and installer distribution only. The source code lives in [samaidev/pcguy](https://github.com/samaidev/pcguy) (private).
