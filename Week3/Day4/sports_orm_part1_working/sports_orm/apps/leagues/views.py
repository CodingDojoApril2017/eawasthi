from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {

		"ascs":Team.objects.filter(league__name__icontains="Atlantic Soccer"),
		"bp":Player.objects.filter(curr_team__team_name__icontains="penguins"),
		"cp":Player.objects.filter(curr_team__league__sport__icontains="baseball"),
		"cb":Player.objects.filter(curr_team__league__name__icontains="american").filter(last_name__icontains="lopez"),
		"fb":Player.objects.filter(curr_team__league__sport__icontains="football"),
		"tms":Team.objects.filter(curr_players__first_name__icontains="sophia"),
		"ams":League.objects.filter(teams__curr_players__first_name__icontains="sophia"),
		"fl":Player.objects.exclude(curr_team__team_name__icontains="Roughriders").filter(last_name__icontains="flores"),
		"stms":Team.objects.filter(all_players__first_name="Samuel"),
		"tiger":Player.objects.filter(all_teams__team_name="Tiger-Cats"),
		"formerly":Player.objects.filter(all_teams__team_name="Vikings").exclude(curr_team__team_name__icontains="Vikings"),
		"jacob":Team.objects.filter(all_players__first_name="Jacob").filter(all_players__last_name="Gray").exclude(curr_players__first_name="Jacob").exclude(curr_players__last_name="Gray"),
		"joshua":Player.objects.filter(all_teams__league__name__icontains="Atlantic Federation of Amateur Baseball Players").filter(first_name="Joshua"),
		."past":Team.objects.annotate(all_players__first_name="Samuel")






	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")








			# "baseballleagues": League.objects.filter(sport__icontains='baseball'),
		# "womenleagues": League.objects.filter(name__icontains='women'),
		# "hockeyleagues": League.objects.filter(sport__icontains='hockey'),
		# "notfootballs": League.objects.exclude(sport__icontains="football"),
		# "atlanticregions": League.objects.filter(name__icontains="atlantic"),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),
		# "conferences": League.objects.filter(name__icontains='conference'),
		# "places": Team.objects.filter(location__icontains='dallas'),
		# "Raptors": Team.objects.filter(team_name__icontains='raptors'),
		# "places": Team.objects.filter(location__icontains='city'),
		# "teams": Team.objects.filter(team_name__startswith="T"),
		# "allteams": Team.objects.order_by("location"),
		# "reverses": Team.objects.order_by("-team_name"),
		# "lasts": Player.objects.filter(last_name__icontains="cooper"),
		# "firsts": Player.objects.filter(first_name__icontains="Joshua"),
		# "coopers": Player.objects.filter(last_name__icontains="cooper").exclude(first_name__icontains='Joshua'),
		# "alexs": Player.objects.filter(first_name__icontains="alexander")|Player.objects.filter(first_name__icontains="Wyatt"),

		#.filter(last_name__icontains="flores")
