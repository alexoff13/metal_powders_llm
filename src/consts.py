NAME_METAL_POWDER_BD = "Наша база металлопорошковых материалов"
NAME_METAL_POWDER_ONTOLOGY = "Онтология базы металлопорошковых материалов"

PATH_TO_METAL_POWDER = "dereviagin.dd@dvfu.ru / Мой Фонд / Загрузки / "

PROMPT = """
Извлеки информацию о материале из текста и представь в JSON. Формат:
{
  "id": "уникальный_числовой_id",
  "name": "Название порошка (например, МПФ-4)",
  "type": "НЕТЕРМИНАЛ",
  "meta": "Описание класса порошка (например, 'Металлический порошок')",
  "comment": "Опционально: ГОСТ, ТУ или примечание (например, 'ГОСТ 6001-79')",
  "successors": [
    {
      "name": "Материал",
      "type": "НЕТЕРМИНАЛ",
      "meta": "Материал",
      "successors": [
        {
          "name": "Название материала (например, 'Магний')",
          "type": "НЕТЕРМИНАЛ",
          "meta": "Материал",
          "successors": []
        }
      ]
    },
    {
      "name": "Химический состав",
      "type": "НЕТЕРМИНАЛ",
      "meta": "Элементы",
      "successors": [ // пример заполнения
        {
          "name": "Fe",
          "type": "НЕТЕРМИНАЛ",
          "meta": "Железо",
          "successors": [
            {
              "value": 0.02,
              "type": "ТЕРМИНАЛ-ЗНАЧЕНИЕ",
              "valtype": "REAL",
              "meta": "Массовая доля, % (max)"
            }
          ]
        },
        {
          "name": "S",
          "type": "НЕТЕРМИНАЛ",
          "meta": "Сера",
          "successors": [
            {
              "value": 0.016,
              "type": "ТЕРМИНАЛ-ЗНАЧЕНИЕ",
              "valtype": "REAL",
              "meta": "Массовая доля, % (max)"
            }
          ]
        }
      ]
    },
    {
      "name": "Применение",
      "type": "НЕТЕРМИНАЛ",
      "meta": "Область использования",
      "successors": [
        {
          "value": "Для электроугольных изделий",//пример значения
          "type": "ТЕРМИНАЛ-ЗНАЧЕНИЕ",
          "valtype": "STRING",
          "meta": "Описание"
        }
      ]
    },
    {
      "name": "Метод получения",
      "type": "НЕТЕРМИНАЛ",
      "meta": "Метод получения",
      "successors": []
    },
    {
      "name": "Гранулометрический состав",
      "type": "НЕТЕРМИНАЛ",
      "meta": "Гранулометрический состав",
      "successors": [
        {
          "name": "Размер частиц",
          "type": "НЕТЕРМИНАЛ",
          "meta": "Размер частиц",
          "successors": []
        },
        {
          "name": "Форма частиц",
          "type": "НЕТЕРМИНАЛ",
          "meta": "Форма частиц",
          "successors": [
            {
              "name": "Преобладающая форма частиц",
              "type": "НЕТЕРМИНАЛ",
              "meta": "Преобладающая форма частиц",
              "successors": []
            }
          ]
        }
      ]
    },
    {
      "name": "Технологические свойства",
      "type": "НЕТЕРМИНАЛ",
      "meta": "Технологические свойства",
      "successors": [
        {
          "name": "Насыпная плотность",
          "type": "НЕТЕРМИНАЛ",
          "meta": "Насыпная плотность",
          "successors": [
            {
              "name": "Числовой интервал",
              "type": "НЕТЕРМИНАЛ",
              "meta": "Числовой интервал",
              "successors": [
                {
                  "name": "Нижняя граница",
                  "type": "НЕТЕРМИНАЛ",
                  "meta": "Нижняя граница",
                  "successors": [
                    {
                      "value": 0.45, // Пример значения
                      "type": "ТЕРМИНАЛ-ЗНАЧЕНИЕ",
                      "valtype": "REAL",
                      "meta": "Числовое значение"
                    }
                  ]
                },
                {
                  "name": "Верхняя граница",
                  "type": "НЕТЕРМИНАЛ",
                  "meta": "Верхняя граница",
                  "successors": [
                    {
                      "value": 0.49, // Пример значения
                      "type": "ТЕРМИНАЛ-ЗНАЧЕНИЕ",
                      "valtype": "REAL",
                      "meta": "Числовое значение"
                    }
                  ]
                }
              ]
            },
            {
              "value": "г/см³", // Единицы измерения
              "type": "ТЕРМИНАЛ-ЗНАЧЕНИЕ",
              "valtype": "STRING",
              "meta": "г/см³"
            }
          ]
        },
        {
          "name": "Сыпучесть",
          "type": "НЕТЕРМИНАЛ",
          "meta": "Сыпучесть",
          "successors": []
        }
      ]
    }
  ]
}
Текст:

"""