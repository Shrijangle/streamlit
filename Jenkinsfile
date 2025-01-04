pipeline {
    agent {
        node {
            label 'jenkins_slave_nodes'
        }
    }

    stages {
        stage('Checkout code') {
            steps {
                git url: 'https://github.com/Shrijangle/streamlit.git', branch: 'main'
            }
        }

        stage('Build Docker Image') { // Moved this inside the 'stages' block
            steps {
                sh 'docker build -t myimage .'
            }
        }

        stage('Build and Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub_credential', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'ech
