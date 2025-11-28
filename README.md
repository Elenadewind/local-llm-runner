local‑llm‑runner

A simple tool to run lightweight language models (LLMs) locally without cloud services. Ideal for privacy, offline use, and testing.
![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue)
![License MIT](https://img.shields.io/badge/license-MIT-green)

Features
* Runs on CPU (no GPU required).
* Supports GGUF models (Llama 2, Mistral, Phi‑3, etc.).
* Minimal dependencies.
* API for integration into your projects.

Installation
Install Python 3.9+:
bash
python --version

Clone the repository:
bash
git clone https://github.com/elenadewind/local-llm-runner.git
cd local-llm-runner

Install dependencies:
bash
pip install -r requirements.txt
Download a GGUF model (e.g., phi-3-mini.gguf) and place it in the models/folder.

Run:
bash
python run.py --model models/phi-3-mini.gguf --temp 0.7 --max-tokens 512
API
After launch, an HTTP server is available: http://localhost:8000

Endpoint:
POST /generate — text generation.

Example request:
json
{
  "prompt": "Tell me about quantum computing",
  "max_tokens": 100
}
Supported Models
* Phi‑3 (4k context)
Mistral 7B (8k context)
Llama 2 7B (4k context)

License
MIT.

Contact
For bug reports and suggestions:
GitHub Issues: 

Commercial Use
A corporate license is required for integration into proprietary products or large‑scale deployment.

Contact us:
Email: rusluvlang@yandex.ru
Available options:
Annual license with support.
White‑label solution.
Customization to meet your requirements.

local‑llm‑runner
Простой инструмент для запуска лёгких языковых моделей (LLM) на вашем устройстве без облачных сервисов. Идеален для приватности, офлайн‑работы и тестирования.

Особенности
Работает на CPU (не требует GPU).
Поддержка моделей формата GGUF (Llama 2, Mistral, Phi‑3 и др.).
Минимальные зависимости.

API для интеграции в ваши проекты.

Установка
Установите Python 3.9+:
bash
python --version
Клонируйте репозиторий:
bash
git clone https://github.com/elenadewind/local-llm-runner.git
cd local-llm-runner
Установите зависимости:
bash
pip install -r requirements.txt
Скачайте модель в формате GGUF (например, phi-3-mini.gguf) и поместите в папку models/.

Запустите:
bash
python run.py --model models/phi-3-mini.gguf --temp 0.7 --max-tokens 512
API
После запуска доступен HTTP‑сервер: http://localhost:8000

Endpoint:
POST /generate — генерация текста.
Пример запроса:
json
{
  "prompt": "Расскажи о квантовых вычислениях",
  "max_tokens": 100
}
Поддерживаемые модели
Phi‑3 (4k context)
Mistral 7B (8k context)
Llama 2 7B (4k context)

Лицензия
MIT.

Контакты
Для сообщений об ошибках и предложений:

GitHub Issues: 

Коммерческое использование
Для интеграции в проприетарные продукты или массового развёртывания требуется корпоративная лицензия.

Свяжитесь с нами:
Email: rusluvlang@yandex.ru

Доступные опции:
Годовая лицензия с поддержкой.
White‑label решение.
Кастомизация под требования.
