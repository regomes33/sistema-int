axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

var app = new Vue({
  el: '#app',
  delimiters: ['${', '}'],
  data: {
    contato: {
      'pk': '',
      'tipo': '',
      'telefone': '',
    },
    veiculos: [],
    veiculo: {
      'pk': '',
      'veiculo_pk': '',
      'veiculo': '',
      'observacao': '',
    },
    comparsas: [],
    comparsa: {
      'pk': '',
      'comparsa_pk': '',
      'parente': '',
      'grau_parentesco': '',
      'observacao': '',
    },
    newcomparsa: {
      'nome': '',
      'rg': '',
      'cpf': '',
      'cnh': '',
    },
    photo: {
      'pk': '',
      'photo': null,
    },
    photo2: {
      'pk': '',
      'photo': null,
      'url': '',
    },
    photoAdd: {
      'pk': '',
      'photo': null,
    },
    tattoo: {
      'pk': '',
      'photo': null,
      'url': '',
    },
    tattooAdd: {
      'pk': '',
      'photo': null,
      'url': '',
    },
    ocorrencias: [],
    ocorrencia: {
      'pk': '',
      'ocorrencia_pk': '',
      'ocorrencia': '',
    },
    naturezas: [],
    operacoes: [],
    qualificacoes: [],
    armas: [],
    status: [],
    infracao: {
      'pk': '',
      'natureza_pk': '',
      'operacao_pk': '',
      'qualificacao': '',
      'arma_pk': '',
      'status': '',
    }
  },
  methods: {
    getContato(url) {
      axios.get(url)
        .then(response => {
          this.contato = response.data
        })
    },
    getVeiculo(url) {
      axios.get(url)
        .then(response => {
          this.veiculo = response.data
        })
      // Pega todos os veiculos de todas as pessoas.
      axios.get(endpoint + 'api/pessoas/veiculos/')
        .then(response => {
          this.veiculos = response.data.data;
        })
    },
    getAddVeiculo() {
      // Pega todos os veiculos de todas as pessoas.
      axios.get(endpoint + 'api/pessoas/veiculos/')
        .then(response => {
          this.veiculos = response.data.data;
        })
    },
    getComparsa(url) {
      axios.get(url)
        .then(response => {
          this.comparsa = response.data
        })
      // Pega todos os comparsas de todas as pessoas.
      axios.get(endpoint + 'api/comparsas/')
        .then(response => {
          this.comparsas = response.data.data;
        })
    },
    getAddComparsa() {
      this.newcomparsa = {
        'nome': '',
        'rg': '',
        'cpf': '',
        'cnh': '',
      }
      // Pega todos os comparsas de todas as pessoas.
      axios.get(endpoint + 'api/comparsas/')
        .then(response => {
          this.comparsas = response.data.data;
        })
    },
    getPhoto(pk) {
      this.photo.pk = pk
    },
    getPhoto2(pk, url) {
      this.photo2.pk = pk
      this.photo2.url = url
    },
    getTattoo(pk, url) {
      this.tattoo.pk = pk
      this.tattoo.url = url
    },
    getOcorrencia(url) {
      axios.get(url)
        .then(response => {
          this.ocorrencia = response.data
        })
      // Pega todas as ocorrencias de todas as pessoas.
      axios.get(endpoint + 'api/pessoas/ocorrencias/')
        .then(response => {
          this.ocorrencias = response.data.data;
        })
    },
    getAddOcorrencia() {
      // Pega todas as ocorrencias de todas as pessoas.
      axios.get(endpoint + 'api/pessoas/ocorrencias/')
        .then(response => {
          this.ocorrencias = response.data.data;
        })
    },
    getInfracao(url) {
      axios.get(url)
        .then(response => {
          this.infracao = response.data
        })
      // Pega todas as naturezas.
      axios.get(endpoint + 'api/naturezas/')
        .then(response => {
          this.naturezas = response.data.data;
        })
      // Pega todas as operacoes.  
        axios.get(endpoint + 'api/operacoes/')
        .then(response => {
          this.operacoess = response.data.data;
        })  
      // Pega todas as qualificacoes.
      axios.get(endpoint + 'api/qualificacoes/')
        .then(response => {
          this.qualificacoes = response.data.data;
        })
      // Pega todas as armas.
      axios.get(endpoint + 'api/armas/')
        .then(response => {
          this.armas = response.data.data;
        })
      // Pega todos os status.
      axios.get(endpoint + 'api/status/')
        .then(response => {
          this.status = response.data.data;
        })
    },
    getAddInfracao(url) {
      // Pega todas as naturezas.
      axios.get(endpoint + 'api/naturezas/')
        .then(response => {
          this.naturezas = response.data.data;
        })
      // Pega todas as operacoes.  
      axios.get(endpoint + 'api/operacoes/')
      .then(response => {
        this.operacoess = response.data.data;
      })    
      // Pega todas as qualificacoes.
      axios.get(endpoint + 'api/qualificacoes/')
        .then(response => {
          this.qualificacoes = response.data.data;
        })
      // Pega todas as armas.
      axios.get(endpoint + 'api/armas/')
        .then(response => {
          this.armas = response.data.data;
        })
      // Pega todos os status.
      axios.get(endpoint + 'api/status/')
        .then(response => {
          this.status = response.data.data;
        })
    },
    salvarAddContato(pessoa_pk) {
      let bodyFormData = new FormData();
      bodyFormData.append('tipo', this.contato.tipo);
      bodyFormData.append('telefone', this.contato.telefone);
      let url = endpoint + 'api/pessoas/' + pessoa_pk + '/contato/add/'
      axios.post(url, bodyFormData)
        .then(response => {
          location.reload();
        })
    },
    salvarContato() {
      let bodyFormData = new FormData();
      bodyFormData.append('tipo', this.contato.tipo);
      bodyFormData.append('telefone', this.contato.telefone);
      let url = endpoint + 'api/pessoas/' + this.contato.pk + '/contato/edit/'
      axios.post(url, bodyFormData)
        .then(response => {
          location.reload();
        })
    },
    salvarAddVeiculo(pessoa_pk) {
      let bodyFormData = new FormData();
      bodyFormData.append('veiculo_pk', this.veiculo.veiculo_pk);
      bodyFormData.append('observacao', this.veiculo.observacao);
      let url = endpoint + 'api/pessoas/' + pessoa_pk + '/veiculo/add/'
      axios.post(url, bodyFormData)
        .then(response => {
          location.reload();
        })
    },
    salvarVeiculo() {
      let bodyFormData = new FormData();
      bodyFormData.append('veiculo_pk', this.veiculo.veiculo_pk);
      bodyFormData.append('observacao', this.veiculo.observacao);
      let url = endpoint + 'api/pessoas/' + this.veiculo.pk + '/veiculo/edit/'
      axios.post(url, bodyFormData)
        .then(response => {
          location.reload();
        })
    },
    salvarAddComparsa(pessoa_pk) {
      let bodyFormData = new FormData();
      bodyFormData.append('comparsa_pk', this.comparsa.comparsa_pk);
      bodyFormData.append('parente', this.comparsa.parente);
      bodyFormData.append('grau_parentesco', this.comparsa.grau_parentesco);
      bodyFormData.append('observacao', this.comparsa.observacao);

      let url = endpoint + 'api/pessoas/' + pessoa_pk + '/comparsa/add/'
      axios.post(url, bodyFormData)
        .then(response => {
          if (response.data.status === 900) {
            console.log(response.data.message);
            alert(response.data.message);
            return
          } else {
            location.reload();
          }
        })
    },
    salvarComparsa() {
      let bodyFormData = new FormData();
      bodyFormData.append('comparsa_pk', this.comparsa.comparsa_pk);
      bodyFormData.append('parente', this.comparsa.parente);
      bodyFormData.append('grau_parentesco', this.comparsa.grau_parentesco);
      bodyFormData.append('observacao', this.comparsa.observacao);
      let url = endpoint + 'api/pessoas/' + this.comparsa.pk + '/comparsa/edit/'
      axios.post(url, bodyFormData)
        .then(response => {
          location.reload();
        })
    },
    salvarAddNewComparsa() {
      let bodyFormData = new FormData();
      bodyFormData.append('newcomparsa', JSON.stringify(this.newcomparsa));
      let url = endpoint + 'api/new-comparsa/add/'
      axios.post(url, bodyFormData)
        .then(response => {
          if (response.data.status === 900) {
            console.log(response.data.message);
            alert(response.data.message);
            return
          } else {
            console.log(response.data);
            this.getAddComparsa()
            this.comparsa.comparsa_pk = response.data.comparsa_pk
            document.getElementById("comparsaCloseModal").click();
          }
        })
    },
    processFile: function(e) {
      this.photo.photo = e.target.files[0]
    },
    processFile2: function(e) {
      this.photo2.photo = e.target.files[0]
    },
    processFileAddPhoto: function(e) {
      this.photoAdd.photo = e.target.files[0]
    },
    processFileTattoo: function(e) {
      this.tattoo.photo = e.target.files[0]
    },
    processFileAddTattoo: function(e) {
      this.tattooAdd.photo = e.target.files[0]
    },
    salvarFoto() {
      let bodyFormData = new FormData();
      bodyFormData.append('photo', this.photo.photo);
      let url = endpoint + 'api/pessoas/' + this.photo.pk + '/photo/edit/'
      axios.post(url, bodyFormData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(response => {
          location.reload();
        })
    },
    salvarFoto2() {
      let bodyFormData = new FormData();
      bodyFormData.append('photo', this.photo2.photo);
      let url = endpoint + 'api/pessoas/' + this.photo2.pk + '/photo/edit/'
      axios.post(url, bodyFormData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(response => {
          location.reload();
        })
    },
    salvarAddFoto(pessoa_pk) {
      let bodyFormData = new FormData();
      bodyFormData.append('photo', this.photoAdd.photo);
      let url = endpoint + 'api/pessoas/' + pessoa_pk + '/photo/add/'
      axios.post(url, bodyFormData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(response => {
          location.reload();
        })
    },
    salvarAddTatuagem(pessoa_pk) {
      let bodyFormData = new FormData();
      bodyFormData.append('tattoo', this.tattooAdd.photo);
      let url = endpoint + 'api/pessoas/' + pessoa_pk + '/tattoo/add/'
      axios.post(url, bodyFormData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(response => {
          location.reload();
        })
    },
    salvarTatuagem() {
      let bodyFormData = new FormData();
      bodyFormData.append('tattoo', this.tattoo.photo);
      let url = endpoint + 'api/pessoas/' + this.tattoo.pk + '/tattoo/edit/'
      axios.post(url, bodyFormData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(response => {
          location.reload();
        })
    },
    salvarAddOcorrencia(pessoa_pk) {
      let bodyFormData = new FormData();
      bodyFormData.append('ocorrencia_pk', this.ocorrencia.ocorrencia_pk);
      let url = endpoint + 'api/pessoas/' + pessoa_pk + '/ocorrencia/add/'
      axios.post(url, bodyFormData)
        .then(response => {
          location.reload();
        })
    },
    salvarOcorrencia() {
      let bodyFormData = new FormData();
      bodyFormData.append('ocorrencia_pk', this.ocorrencia.ocorrencia_pk);
      let url = endpoint + 'api/pessoas/' + this.ocorrencia.pk + '/ocorrencia/edit/'
      axios.post(url, bodyFormData)
        .then(response => {
          location.reload();
        })
    },
    salvarAddInfracao(pessoa_pk) {
      let bodyFormData = new FormData();
      bodyFormData.append('natureza_pk', this.infracao.natureza_pk)
      bodyFormData.append('operacao_pk', this.infracao.operacao_pk)
      bodyFormData.append('qualificacao', this.infracao.qualificacao)
      bodyFormData.append('arma_pk', this.infracao.arma_pk)
      bodyFormData.append('status', this.infracao.status)
      let url = endpoint + 'api/pessoas/' + pessoa_pk + '/infracao/add/'
      axios.post(url, bodyFormData)
        .then(response => {
          location.reload();
        })
    },
    salvarInfracao() {
      let bodyFormData = new FormData();
      bodyFormData.append('natureza_pk', this.infracao.natureza_pk)
      bodyFormData.append('operacao_pk', this.infracao.operacao_pk)
      bodyFormData.append('qualificacao', this.infracao.qualificacao)
      bodyFormData.append('arma_pk', this.infracao.arma_pk)
      bodyFormData.append('status', this.infracao.status)
      let url = endpoint + 'api/pessoas/' + this.infracao.pk + '/infracao/edit/'
      axios.post(url, bodyFormData)
        .then(response => {
          location.reload();
        })
    },
  }
});