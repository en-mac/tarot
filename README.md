# tarot

# dir
tarot-app/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── cards.py
│   │   │   ├── history.py
│   │   │   ├── about.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── card_service.py
│   │   │   ├── auth_service.py
│   │   │   ├── fortune_service.py
│   │   ├── db.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── card.py
│   │   │   ├── fortune.py
│   │   ├── utils.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── manage.py
│
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   ├── favicon.ico
│   ├── src/
│   │   ├── assets/
│   │   │   ├── images/
│   │   │   │   ├── tarot-back.jpg
│   │   │   │   ├── tarot-fronts/
│   │   │   │   │   ├── card1.jpg
│   │   │   │   │   ├── card2.jpg
│   │   │   │   │   └── ...
│   │   ├── components/
│   │   │   ├── About.jsx
│   │   │   ├── DrawCard.jsx
│   │   │   ├── FortuneHistory.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Navbar.jsx
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   ├── services/
│   │   │   ├── api.js
│   │   ├── App.jsx
│   │   ├── index.js
│   │   ├── index.css
│   ├── Dockerfile
│   ├── tailwind.config.js
│   ├── package.json
│   └── yarn.lock
│
├── deployments/
│   ├── k8s/
│   │   ├── backend-deployment.yaml
│   │   ├── backend-service.yaml
│   │   ├── frontend-deployment.yaml
│   │   ├── frontend-service.yaml
│   │   ├── ingress.yaml
│   ├── docker-compose.yaml
│
├── .gitignore
├── README.md
└── LICENSE
