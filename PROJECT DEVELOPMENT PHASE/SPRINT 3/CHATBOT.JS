<script>
  window.watsonAssistantChatOptions = {
    integrationID: "ee05ce57-7bbf-4d99-916c-70ef5910310a", // The ID of this integration.
    region: "au-syd", // The region your integration is hosted in.
    serviceInstanceID: "3949a985-fb2d-4cdd-ab07-7faf988090c3", // The ID of your service instance.
    onLoad: function(instance) { instance.render(); }
  };
  setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
  });
</script>
