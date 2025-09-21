"""
Простое веб-приложение для отображения HTML-страниц.
Использует функцию open() для чтения файлов.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Определяем какой файл показывать
        if self.path == '/':
            file_path = 'templates/index.html'
        elif self.path == '/catalog':
            file_path = 'templates/catalog.html'
        elif self.path == '/category':
            file_path = 'templates/category.html'
        elif self.path == '/contacts':
            file_path = 'templates/contacts.html'
        else:
            self.send_error(404, 'Страница не найдена')
            return

        # Читаем файл через open() как требует задание
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))

        except FileNotFoundError:
            self.send_error(404, 'Файл не найден')
        except Exception as e:
            self.send_error(500, f'Ошибка сервера: {str(e)}')

    def do_POST(self):
        """Обработка POST запросов для формы контактов"""
        if self.path == '/contacts':
            # Получаем длину данных
            content_length = int(self.headers.get('Content-Length', 0))
            # Читаем данные
            post_data = self.rfile.read(content_length).decode('utf-8')
            # Парсим данные формы
            parsed_data = urllib.parse.parse_qs(post_data)

            # Печатаем данные в консоль
            print("=" * 50)
            print("POST ДАННЫЕ ОТ ПОЛЬЗОВАТЕЛЯ:")
            for key, values in parsed_data.items():
                print(f"{key}: {values[0]}")
            print("=" * 50)

            # Перенаправляем обратно на контакты
            self.send_response(303)  # 303 See Other
            self.send_header('Location', '/contacts')
            self.end_headers()
        else:
            self.send_error(404, 'Страница не найдена')


def run_server(port=8000):
    """Запускает HTTP сервер"""
    server = HTTPServer(('', port), SimpleHandler)
    print(f'✅ Сервер запущен: http://localhost:{port}')
    print('⏹️  Нажмите Ctrl+C для остановки')

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n🛑 Сервер остановлен')


if __name__ == '__main__':
    run_server()
