
# my-YAML-course

An interface for a YAML databse.

This is a fastapi webserver that allows us to perform CRUD operations on YAML files.
and can be refered to as a YAMLhouse or a YAML warehouse.

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

To run this project, you will need to add the following environment variables to your .env file

`PYTHONPATH` should point to the root directory of the project


## Run Locally

Clone the project

```bash
  git clone https://github.com/emarco177/my-YAML-course
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
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.udemy.com/user/eden-marco/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eden-marco)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/EdenEmarco177)



