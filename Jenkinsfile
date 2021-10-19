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
 
        //  run program 
        stage ('Build') {
            steps {
                script {
                    main.py 
 
            }
        }
    }
}