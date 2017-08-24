<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/marked/0.3.6/marked.min.js"></script>

<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-T8Gy5hrqNKT+hzMclPo118YTQO6cYprQmhrYwIiQ/3axmI1hQomh7Ud2hPOy8SP1" crossorigin="anonymous">

<script type="text/javascript" charset="utf-8">
  $(document).ready(function() {
    $(".content-markdown").each(function () {
      var content = $(this).text()
      var markedContent = marked(content)
      $(this).html(markedContent)


    })
    $(".post-detail-item img").each(function () {
      $(this).addClass("img-responsive")
    })



    var contentInput  = $("#id_content");


    function setContent(value) {
      var markedContent = marked(value);
      $("#preview-content").html(markedContent);
      $("#preview-content img").each(function () {
        $(this).addClass("img-responsive");
      })
    }
    setContent(contentInput.val());

    contentInput.keyup(function () {
      var newContent = $(this).val();
      setContent(newContent);
    })

    var titleInput = $("#id_title");


    function setTitle(value) {
      $("#preview-title").text(value)
    }
    setTitle(titleInput.val())
    $("#preview-title").text(titleInput.val())
    titleInput.keyup(function () {
      var newTitle = $(this).val()
      setTitle(newTitle)
    })

    $('.comment-reply-btn').click(function (event) {
      event.preventDefault()
      $(this).parent().next(".comment-reply").fadeToggle()
})


  })
</script>
