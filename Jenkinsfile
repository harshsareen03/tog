pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/user/todo-app.git'
            }
        }

        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t todo-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 8000:8000 todo-app'
            }
        }
    }
}