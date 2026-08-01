"""
MARF Text To Speech
Generate Bengali voice using Edge-TTS.
"""

from __future__ import annotations

import asyncio
from pathlib import Path

import edge_tts

from src.config import TTS, OUTPUT


class BengaliTTS:
    def __init__(self):
        self.voice = TTS.get("voice", "bn-BD-NabanitaNeural")
        self.speed = TTS.get("speed", "+0%")

    async def _generate(self, text: str, output_file: str):
        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice,
            rate=self.speed,
        )
        await communicate.save(output_file)

    def save(self, text: str, filename: str = "voice.mp3") -> str:
        output_dir = Path(OUTPUT.get("folder", "output"))
        output_dir.mkdir(parents=True, exist_ok=True)

        output_path = output_dir / filename

        asyncio.run(
            self._generate(
                text=text,
                output_file=str(output_path),
            )
        )

        return str(output_path)


if __name__ == "__main__":
    tts = BengaliTTS()

    audio = tts.save(
        "আসসালামু আলাইকুম। এটি MARF-এর প্রথম বাংলা ভয়েস টেস্ট।"
    )

    print("Audio saved:", audio)
