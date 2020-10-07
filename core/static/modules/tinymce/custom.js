let default_init = {
    'referrer_policy': 'origin',
    // 'icons_url': 'https://www.example.com/icons/material/icons.js',
    // 'icons': 'material',
    'height': 500,
    'plugins': "autosave,advlist,charmap,codesample,code,image,imagetools,media,lists,preview,print,table,spellchecker," +
        "paste,searchreplace,pagebreak,wordcount,visualblocks,visualchars,emoticons,autolink,link",
    'toolbar1': 'undo redo|fontsizeselect forecolor styleselect|bold italic underline|' +
        'alignjustify alignleft aligncenter alignright alignnone|indent outdent|bullist numlist|',
    'toolbar2': 'code charmap emoticons|image media link|rotateleft rotateright|flipv fliph|editimage imageoptions|preview print|' +
        'pagebreak|wordcount visualblocks visualchars',
    'toolbar_mode': 'sliding',
    'toolbar_sticky': true,
    'theme': "silver",
    'skin': 'oxide',
    'custom_undo_redo_levels': 10,
    'placeholder': "Start editing. . .",
    'image_advtab': true,
    'image_description': true,
    'image_title': true,
    'image_uploadtab': true,
    // 'image_prepend_url': 'MEDIA_URL',
    'images_upload_url': '/upload/',

}

for (var i = 0; i < tinymce.editors.length; i++) {
	  var editorInstance = tinymce.editors[i];
	  editorInstance.setContent('I have changed the content of editor ' + i + '!');
	}
let first_init = jQuery.extend({}, default_init);
first_init.selector = ".first_textarea";
tinymce.init(first_init);

let second_init = jQuery.extend({}, default_init);
second_init.selector = ".second_textarea";
tinymce.init(second_init);