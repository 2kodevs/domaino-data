function refresh_charts(){
  setTimeout(function start (){
    
    $('.bar').each(function(i){  
      var $bar = $(this);
      $(this).append('<span class="count"></span>')
      setTimeout(function(){
        $bar.css('width', $bar.attr('data-percent'));      
      }, i*100);
    });

    $('.count').each(function () {
        $(this).prop('Counter',0).animate({
            Counter: $(this).parent('.bar').attr('data-percent')
        }, {
            duration: 2000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now) +'%');
            }
        });
    });

  }, 500);
};

function new_bar(parity, label, percent){
  var cls = ['label', 'label second'];
  return `<div class="bar" data-percent="${percent}%"><span class="${cls[parity]}">${label}</span></div>\n`
};

function load(json){
  //TODO: get the json and remove the function argument
  var val = document.getElementById('strategy').value;
  if(val in json){
    document.getElementById('main-label').innerHTML = val;
    var data = json[val];

    var p = 0;
    var lines = "";
    for(var key in data){
      if(key !== val){
        lines += new_bar(p, key, data[key]);
        p = 1 - p;
      }
    }
    document.getElementById('holder').innerHTML = lines;
    refresh_charts();
  }
};

function populate_select(json){
  //TODO: get the json and remove the function argument
  var sel = document.getElementById('strategy');
  lines = "";
  for(var key in json){
    lines += `<option value="${key}">${key}</option>\n`;
  }
  sel.innerHTML = lines;
};
