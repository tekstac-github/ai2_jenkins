pipeline {
    agent any

    environment {
        VENV = 'jenkins-ai-env'
    }

    stages {
        stage('Clean Workspace') {
            steps {
                script {
                    sh 'rm -rf ${WORKSPACE}/*'
                }
            }
        }

        stage('Set Up Environment') {
            steps {
                script {
                    sh 'sudo apt install -y python3-virtualenv'
                    sh 'virtualenv ${VENV}'
                    sh '. ${VENV}/bin/activate && pip install --upgrade pip'
                    sh '. ${VENV}/bin/activate && pip install pandas scikit-learn numpy joblib matplotlib seaborn'
                }
            }
        }

        stage('Train AI Model') {
            steps {
                script {
                    try {
                        sh '. ${VENV}/bin/activate && python train_failure_model.py'
                    } catch (Exception e) {
                        echo 'Model training failed!'
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }

        stage('Predict Failure') {
            steps {
                script {
                    def prediction = ''
                    try {
                        prediction = sh(script: '. ${VENV}/bin/activate && python predict_failure.py', returnStdout: true).trim()
                        echo "AI Prediction: ${prediction}"
                    } catch (Exception e) {
                        echo 'Prediction failed!'
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }

        stage('Visualize Results') {
            steps {
                script {
                    sh '. ${VENV}/bin/activate && python visualize_results.py'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline encountered an error!'
        }
        always {
            archiveArtifacts artifacts: 'failure_prediction_model.pkl', onlyIfSuccessful: true
            sh 'deactivate'
        }
    }
}
