pipeline {
    agent any

    stages {
        stage('Set Up Environment') {
            steps {
                script {
                    sh 'sudo apt install python3-virtualenv'
                    sh 'pip install virtualenv'
                    sh 'virtualenv jenkins-ai-env'
                    sh '. jenkins-ai-env/bin/activate'
                    sh 'pip install pandas scikit-learn numpy joblib'
                }
            }
        }

        stage('Train AI Model') {
            steps {
                script {
                    sh '. jenkins-ai-env/bin/activate && python train_failure_model.py'
                }
            }
        }

        stage('Predict Failure') {
            steps {
                script {
                    def prediction = sh(script: '. jenkins-ai-env/bin/activate && python predict_failure.py', returnStdout: true).trim()
                    echo "AI Prediction: ${prediction}"
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'failure_prediction_model.pkl', onlyIfSuccessful: true
        }
    }
}
