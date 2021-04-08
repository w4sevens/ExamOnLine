function CmsNewsList() {

}


CmsNewsList.prototype.initDataPicker = function(){
    var startPicker = $('#id_start_date');
    var endPicker = $('#id_graduate_date');
    var todayDate = new Date();
    var todayStr = todayDate.getFullYear() + '-' + (todayDate.getMonth()+1) + '-' + todayDate.getDate();
    var options = {
        'showButtonPanel': true,
        'format': 'yy-mm-dd',
        'startDate': '',
        'endDate': todayStr,
        'language': 'zh-CN',
        'todayBtn': 'linked',
        'todayHighlight':true,
        'clearBtn': true,
        'autoclose':true,
    };

    startPicker.datepicker(options);
    endPicker.datepicker(options);
};

CmsNewsList.prototype.run = function () {
    this.initDataPicker();
};

$(function () {
   var newsList = new CmsNewsList();
   newsList.run();
});
