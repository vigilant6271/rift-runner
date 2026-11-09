# 🎮 RIFT RUNNER

A complete 2D action platformer built with pure HTML5 Canvas + Web Audio API — no frameworks, no dependencies.

## 🕹️ Play Now

**[▶ Play in Browser](https://vigilant6271.github.io/rift-runner/game.html)**

## Features

| System | Details |
|---|---|
| **3 Levels** | Neon City · Overgrown Ruins · Industrial Core |
| **4 Enemy Types** | Scout Drone · Enforcer · Rift Stalker · Siege Unit |
| **2 Bosses** | The Iron Warden · The Rootmind (multi-phase) |
| **Movement** | Run · Jump · Double Jump · Dash · Coyote Time · Jump Buffering |
| **Combat** | Melee attack · Special ability (slow-mo field) · Invincibility frames |
| **HUD** | Health bar · Energy bar · Crystal count · Boss HP bar · Cooldown indicators |
| **Menus** | Logo screen · Main menu · Options (Audio/Graphics/Accessibility) · Pause · Credits |
| **Save System** | Auto-saves at checkpoints via localStorage |
| **Particles** | Hit sparks · Dash trails · Death explosions · Pickups |
| **Audio** | Procedural Web Audio API — music + SFX per biome |

## Controls

| Key | Action |
|---|---|
| `A` / `D` or `←` / `→` | Move |
| `Space` | Jump (press twice for double jump) |
| `J` | Attack |
| `K` | Special ability |
| `Shift` | Dash |
| `E` | Interact |
| `Esc` | Pause |

## Android APK

The `android/` folder is a complete Gradle project ready to build:

```bash
# Open in Android Studio, or:
cd android
./gradlew assembleDebug
# → app/build/outputs/apk/debug/app-debug.apk
```

Requires Android SDK + Java 11+. See `android/build_apk.py` for full instructions.

## Tech Stack

- HTML5 Canvas (2D rendering)
- Web Audio API (procedural music + SFX)
- Vanilla JavaScript (no frameworks)
- localStorage (save system)
- Android WebView (APK wrapper)

## Based On

Built from the **AI 2D Platformer Game Formula** — a complete game design framework covering 25 systems from core identity through technical architecture.

---

*© 2026 Kiro Studios*
