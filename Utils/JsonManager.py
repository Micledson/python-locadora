import json
import os


class JsonManager:

    def open(self, filePath: str):
        path = os.getcwd() + filePath

        isExists = os.path.isfile(path)

        if isExists:
            with open(path) as file:
                data = json.load(file)
                file.close()
                return data
        else:
            return self._createJson(path)

    def update(self, filePath: str, data):
        path = os.getcwd() + filePath

        isExists = os.path.isfile(path)

        if isExists:
            with open(path, 'w') as file:
                json.dump(data, file, indent=2, separators=(',', ': '))
                file.close()
        else:
            self._createJson(path)

    def _createJson(self, filePath: str):
        with open(filePath, 'w') as file:
            json.dump([], file, indent=2, separators=(',', ': '))
            file.close()
            return []
