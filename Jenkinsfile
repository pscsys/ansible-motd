pipeline {

  agent any 

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
