axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

var app = new Vue({
  el: '#app',
  delimiters: ['${', '}'],
  data: {
    pessoa: {
      'nome': '',
      'sobrenome': '',
      'apelido': '',
      'mae': '',
      'pai': '',
      'faccao': '',
      'nascimento': '',
      'cpf': '',
      'rg': '',
      'cnh': '',
      'address': '',
      'address_number': '',
      'complement': '',
      'district': '',
      'cep': '',
      'country': 'Brasil',
    },
    pessoas: [],
    districts: [],
    faccoes: [],
    naturezas: [],
    qualificacoes: [],
    armas: [],
    status: [],
    photos: [],
    fotos: [{
      'foto': '',
    }],
    tattoos_list: [],
    tattoos: [{
      'tattoo': '',
    }],
    infracao_id: 1,
    infracoes: [{
      'id': 1,
      'natureza': '',
      'qualificacao': '',
      'arma': '',
      'status': '',
    }],
    carros: [],
    veiculo_id: 1,
    veiculos: [{
      'id': 1,
      'veiculo': ''
    }],
    ocorrencias_list: [],
    ocorrencia_id: 1,
    ocorrencias: [{
      'id': 1,
      'ocorrencia': ''
    }],
    tipos: [],
    contato_id: 1,
    contatos: [{
      'id': 1,
      'tipo': '',
      'telefone': '',
    }],
    comparsa_id: 1,
    comparsas: [{
      'id': 1,
      'nome': '',
      'cpf': '',
      'rg': '',
      'cnh': '',
      'parente': '',
      'grau_parentesco': '',
      'observacao': '',
    }],
    v: [
      { 'v1': false },
      { 'v2': false },
      { 'v3': false },
      { 'v4': false },
      { 'v5': false },
      { 'v6': false },
      { 'v7': false },
      { 'v8': false },
      { 'v9': false },
      { 'v10': false },
    ]
  },
  created() {
    axios.get(endpoint + 'api/naturezas/')
      .then(response => {
        this.naturezas = response.data.data;
      })

    axios.get(endpoint + 'api/districts/')
      .then(response => {
        this.districts = response.data.data;
      })

    axios.get(endpoint + 'api/faccoes/')
      .then(response => {
        this.faccoes = response.data.data;
      })

    axios.get(endpoint + 'api/qualificacoes/')
      .then(response => {
        this.qualificacoes = response.data.data;
      })

    axios.get(endpoint + 'api/armas/')
      .then(response => {
        this.armas = response.data.data;
      })

    axios.get(endpoint + 'api/status/')
      .then(response => {
        this.status = response.data.data;
      })

    axios.get(endpoint + 'api/veiculos/')
      .then(response => {
        this.carros = response.data.data;
      })

    axios.get(endpoint + 'api/ocorrencias/')
      .then(response => {
        this.ocorrencias_list = response.data.data;
      })

    axios.get(endpoint + 'api/tipo_telefone/')
      .then(response => {
        this.tipos = response.data.data;
      })
  },
  methods: {
    notifyError(title, message) {
      $.notify({
        title: title,
        message: message
      }, {
        element: 'body',
        type: 'error',
        allow_dismiss: true,
        newest_on_top: true,
        placement: {
          align: 'right'
        },
        offset: 20,
        spacing: 10,
        z_index: 9999,
        delay: 5000,
        timer: 1300,
        animate: {
          enter: 'animated fadeIn',
          exit: 'animated fadeOutDown'
        }
      });
    },
    fotoAdd() {
      this.fotos.push({
        'foto': '',
      })
    },
    tattooAdd() {
      this.tattoos.push({
        'tattoo': '',
      })
    },
    infracaoAdd() {
      this.infracao_id++;
      this.infracoes.push({
        'id': this.infracao_id,
        'natureza': '',
        'qualificacao': '',
        'arma': '',
        'status': '',
      })
    },
    ocorrenciaAdd() {
      this.ocorrencia_id++;
      this.ocorrencias.push({
        'id': this.ocorrencia_id,
        'ocorrencia': '',
      })
    },
    contatoAdd() {
      this.contato_id++;
      this.contatos.push({
        'id': this.contato_id,
        'tipo': '',
        'telefone': '',
      })
    },
    comparsaAdd() {
      this.comparsa_id++;
      this.comparsas.push({
        'id': this.comparsa_id,
        'nome': '',
        'cpf': '',
        'rg': '',
        'cnh': '',
        'parente': '',
        'grau_parentesco': '',
        'observacao': '',
      })
    },
    veiculoAdd() {
      this.veiculo_id++;
      this.veiculos.push({
        'id': this.veiculo_id,
        'veiculo': '',
      })
    },
    processFile: function(e) {
      this.photos.push(e.target.files[0])
    },
    processFileTattoo: function(e) {
      this.tattoos_list.push(e.target.files[0])
    },
    salvar(e) {
      let bodyFormData = new FormData();
      bodyFormData.append('pessoa', JSON.stringify(this.pessoa));

      this.photos.forEach((file, i) => {
        bodyFormData.append('photos[' + i + ']', file);
      });

      this.tattoos_list.forEach((file, i) => {
        bodyFormData.append('tattoos[' + i + ']', file);
      });

      bodyFormData.append('infracoes', JSON.stringify(this.infracoes));
      bodyFormData.append('ocorrencias', JSON.stringify(this.ocorrencias));
      bodyFormData.append('contatos', JSON.stringify(this.contatos));
      bodyFormData.append('comparsas', JSON.stringify(this.comparsas));
      bodyFormData.append('veiculos', JSON.stringify(this.veiculos));

      axios.post(endpoint + 'api/pessoas/add/', bodyFormData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(response => {
          if (response.data.status_code == 500) {
            Object.keys(response.data).forEach(key => {
              if (key == 'status_code') return;
              this.notifyError(key, response.data[key][0]);
            });
            return
          }

          if (response.data.status_code == 900) {
            this.notifyError('Erro', response.data.message)
            return
          }

          location.href = endpoint + 'pessoa/'
        })
    },
    toggleCollapse(v) {
      Object.keys(this.v).forEach(item => { 
        if (item != 'v' + v) {
          Vue.set(this.v, item, false);
        }
      });

      Vue.set(this.v, 'v' + v, !this.v['v' + v]);
    }
  }
});