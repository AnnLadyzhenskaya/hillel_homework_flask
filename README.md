# hillel_homework_flask

<p>Install all <i>requirements</i> via command: <code>pip install -r requirements.txt</code>
</p>

<p><i>Run</i> the API: <code>flask --app app run</code></p>

<p>You can find <i>postman collection</i> in the <code>/postman</code> folder</p>

<p><b>API routes:</b></p>

<li><code>GET /requirements/</code>:</li>
Returns all requirements from <code>requirements.txt</code> file.
<br>
Response example:

```json
{
    "Faker": "17.0.0",
    "Flask": "2.2.3",
    "pandas": "1.5.3",
    "requests": "2.28.2"
}
```

<li><code>GET /generate-users/?count=n</code>:</li>
Returns json with automatically generated users.
<br>
<code>GET</code> parameter <code>count</code> is optional (100 by default)
<br>
Response example:

```json
[
    {
        "email": "evan93@example.net",
        "name": "George"
    },
    {
        "email": "tammysmith@example.org",
        "name": "Kaitlin"
    }
]
```

<li><code>GET /mean/</code>:</li>
Returns json with average values from hw.csv file.
<br>
Response example:

```json
{
    "avg_height_cm": 172.7,
    "avg_weight_kg": 57.64
}
```

<li><code>GET /space/</code>:</li>
Returns json with number of astronauts in space.
<br>
Response example:

```json
{
    "Astronauts count": 10
}
```