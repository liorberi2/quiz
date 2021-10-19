pipeline {
    agent any
 
        // 1. Check if 'main.py' exists, 
        stage ('Build') {
            steps {
                script {
                    if (fileExists('main.py') == false) {
                        unstable('Code file not found!')
                    }
                }
            }
        }
        // 2. Dummy deploy
        // Print a message (only done if the build is stable)
        stage ('Deploy') {
            when { not { equals expected: 'UNSTABLE
            steps {
                echo 'Deploying it gently...'
            }
        }
    }
}