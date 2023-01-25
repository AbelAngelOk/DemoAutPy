pipeline {
  agent any

  }
  stages {
    stage('init') {
      steps {
        sh "python --version"
        sh "python -m venv entorno"
        sh "dir entorno"
        sh "entorno\\Scripts\\activate"
        sh "python --version"
        sh "where python"
        sh "pip -V"
        sh "pip install -r requirements.txt"
      }
    }

    stage('Test') {
      steps {
        sh "pytest"
      }
    }

  }
}
