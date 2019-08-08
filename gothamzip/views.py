from django.shortcuts import render
from django.views.generic import FormView
from gothamzip.forms import ZipForm


class ZipCheckView(FormView):
    template_name = "gothamzip.html"
    form_class = ZipForm

    def form_valid(self, form):
        zipcode = form.cleaned_data.get("zip")
        return self.render_to_response(self.get_context_data(form=form, zip=zipcode))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form, error=True))
