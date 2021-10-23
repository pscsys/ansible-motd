pipeline {

  agent {
    label 'agent'
  }

  stages {

    stage ('Molecule test') {
      steps {
        sh '''
          molecule test
        '''
      }
    }
  }
}
