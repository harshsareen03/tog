pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/harshsareen03/tog.git'
            }
        }

        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t todo-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop todo-app || true
                docker rm todo-app || true
                
                docker run -d \ --name todo-app -p 8000:8000 todo-app
                '''
            }
        }
    }
}