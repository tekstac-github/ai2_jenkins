pipeline {
    agent any

    environment {
        VENV = 'jenkins-ai-env'
    }

    stages {
        stage('Clean Workspace') {
            steps {
                script {
                    sh 'find ${WORKSPACE} -mindepth 1 ! -name "train_failure_model.py" ! -name "predict_failure.py" ! -name "visualize_results.py" ! -name "jenkins_build_data.csv" -delete'
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
                        if (!fileExists('jenkins_build_data.csv')) {
                            error 'Training data file not found: jenkins_build_data.csv'
                        }
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
                        if (!fileExists('failure_prediction_model.pkl')) {
                            error 'Model file not found: failure_prediction_model.pkl'
                        }
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
                    try {
                        if (fileExists('visualize_results.py')) {
                            sh '. ${VENV}/bin/activate && python visualize_results.py'
                            // Archive the graph so it’s accessible in Jenkins
                            archiveArtifacts artifacts: 'build_results_comparison.png', onlyIfSuccessful: true
                            echo 'Visualization complete! View the graph here:'
                            echo "${env.BUILD_URL}artifact/build_results_comparison.png"
                        } else {
                            echo 'Visualization script not found, skipping visualization.'
                        }
                    } catch (Exception e) {
                        echo 'Visualization failed!'
                        currentBuild.result = 'FAILURE'
                    }
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
            sh '[ -n "$VIRTUAL_ENV" ] && deactivate || true'
        }
    }
}
