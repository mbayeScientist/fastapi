
#inspiré par le cours de Eden Udemy(Merci)

## API Reference

#### Get all items

```http
  POST /api/yamls
```

| Payload | Type     | Description                |
| :-------- | :------- | :------------------------- |
|  YAML| `data-raw` (x-yaml header) | **Required**. Your YAML file |

#### Validates the YAML and saves it in the DB if exists (returns document uuid)

```http
  GET /api/yamls/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of document to fetch |

#### Returns the YAML document as a JSON (if exists)


## Environment Variables

creer un fichier .env

`PYTHONPATH`="repo principal"  ajouter le dans .env


## Run Locally

Clone the project

```bash
  git clone https://github.com/mbayeScientist/fastapi.git
```

Go to the project directory

```bash
  cd my_yaml_course
```

Install dependencies

```bash
  pipenv install
```

Start the server

```bash
  python app.py
```


## Running Tests

To run tests, run the following command

```bash
  pytest . -s -v
```


## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mouhamed-mbaye-87184a18b/)




