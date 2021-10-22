pipeline {

  agent any 

  stages {

    stage ('Molecule test') {
      steps {
        sh '''
          export PATH="$PATH:/var/lib/jenkins/.local/bin"
          molecule test
        '''
      }
    }
  }
}
