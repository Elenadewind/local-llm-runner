# local-llm-runner
Простой инструмент для запуска лёгких языковых моделей (LLM) на вашем устройстве без облачных сервисов. Идеален для приватности, офлайн‑работы и тестирования.
## Особенности - Работает на CPU (не требует GPU). 
- Поддержка моделей GGUF (Llama 2, Mistral, Phi‑3 и др.).
-  - Минимальные зависимости.
   - - API для интеграции в ваши проекты.
     -  ## Установка
     -  1. Установите Python 3.9+: ```bash python --version
        2.  Клонируйте репозиторий: bash git clone https://github.com/elenadewind/local-llm-runner.git cd local-llm-runner
        3.   Установите зависимости: bash pip install -r requirements.txt
        4.   Скачайте модель в формате GGUF (например, ) и поместите в папку models/.
        5.    Запуск bash python run.py --model models/phi-3-mini.gguf --temp 0.7 --max-tokens 512
          API
          После запуска доступен HTTP‑сервер (http://localhost:8000):
           POST /generate — генерация текста.
          Пример запроса: json {"prompt": "Расскажи о квантовых вычислениях", "max_tokens": 100}
          Поддерживаемые модели
           Phi‑3 (4k context)
           Mistral 7B (8k context)
           Llama 2 7B (4k context)
          Лицензия MIT
           Контакты
                    Issues:
          ## Коммерческое использование

Для интеграции в проприетарные продукты или массового развёртывания требуется корпоративная лицензия. 

Свяжитесь: Email: rusluvlang@yandex.ru

Доступные опции:
- Годовая лицензия с поддержкой.
- White‑label решение.
- Кастомизация под требования.
          
