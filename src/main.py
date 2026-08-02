"""
MARF Main Entry Point
"""

from src.logger import logger
from src.config import PROJECT


def main():
    logger.info("MARF started")

    print("=" * 40)
    print(PROJECT.get("name", "MARF"))
    print(f"Version: {PROJECT.get('version', '1.0.0')}")
    print("System initialized successfully.")
    print("=" * 40)

    logger.info("MARF finished successfully")


if __name__ == "__main__":
    main()
