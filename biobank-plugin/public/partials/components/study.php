<h4><a href='#study-<?= $study->study->study_id ?>' data-toggle="collapse"
	   role="button" aria-expanded="false" aria-controls="collapseExample">
	   <?= $study->study->name ?>
    </a></h4>
<form class="<?= $this->plugin_name ?>-form" id="consent-form-<?= $study->study->study_id ?>"
	  method="post" name="consent_form" action=<?php echo esc_url(admin_url("admin-post.php")); ?>>
	<input type="hidden" name="action" value="consent_form">
	<?php wp_nonce_field("consent_form", "consent_nonce"); ?>


	<div id='study-<?= $study->study->study_id ?>' class='collapse'>
		<p class="biobank-description"><?= $study->study->description ?></p>
		<p class="biobank-homepage"><a href="<?= $study->study->homepage ?>" target="_blank">Read more</a></p>
		<div class='row'>
			<div class='col-md-5 text-md-right'>
				<label for="<?= $this->plugin_name ?>-study-<?= $study->study->study_id ?>">Participate</label>
			</div>
			<div class='col-md-7 collapse'>
				<input name='<?= $this->plugin_name ?>[study][<?= $study->study->study_id ?>][consent]' type='hidden' value='0'>
				<input id = '<?= $this->plugin_name ?>-study-<?= $study->study->study_id ?>' name = '<?= $this->plugin_name ?>[study][<?= $study->study->study_id ?>][consent]' type = 'checkbox' <?= $consent === True ? "checked" : "" ?>>
			</div>
		</div>

		<div class='row'>
			<div class='col-md-7 offset-md-5'>
				<input type = "submit" class = "btn btn-primary float-left" />
			</div>
		</div>
	</div>
</form>
