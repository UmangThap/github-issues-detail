;(function () {
	var ajaxReq = function(url, type, data){
		return $.ajax({
			url: url,
			type: type,
			data: data
		})
	}

	function getIssues(){
        var url = '/get_all_issues/';
        var repoUrl = $('.repo-url').val();
		var data = { 'url' : repoUrl };
        var req = ajaxReq(url, 'POST', data);
        $.when(req).done(function(data){
            $('#total-issues').text(data.total_issue);
            $('#day-issue').text(data.issue_in_day);
            $('#seven-day-issue').text(data.issue_in_seven_day);
            $('#remaining-issue').text(data.issue_before_seven_day);
        })
	}
    $(document).ready(function(){
        console.log('here');
    	$('#submit-url').click(getIssues)
	}) 
})()
