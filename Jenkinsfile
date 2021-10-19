pipeline {
    agent any
	
  // clean environment with new files
  stages {
    stage('Checkout') {
      steps {
        cleanWs()
        checkout scm
      }
    }
 
  stage('build') {
    steps {
        sh 'python main.py'
    }
}