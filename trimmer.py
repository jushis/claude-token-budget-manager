import os
import sys

def trim_codebase(directory_path):
    """Сканирует папку проекта и собирает код в один файл для ИИ, удаляя лишний мусор."""
    ignore_dirs = {'.git', '__pycache__', 'node_modules', 'venv', '.env', 'dist'}
    ignore_extensions = {'.pyc', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico', '.mp4'}
    
    combined_text = ""
    
    for root, dirs, files in os.walk(directory_path):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        for file in files:
            if any(file.endswith(ext) for ext in ignore_extensions):
                continue
                
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Удаляем пустые строки для экономии токенов контекста
                compact_content = "\n".join([line for line in content.splitlines() if line.strip()])
                combined_text += f"\n\n--- FILE: {file_path} ---\n{compact_content}"
            except Exception:
                pass # Пропускаем бинарные файлы
                
    with open("ai_ready_context.txt", "w", encoding='utf-8') as out:
        out.write(combined_text)
    print("Готово! Файл ai_ready_context.txt создан для отправки в Claude.")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    trim_codebase(path)
