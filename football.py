#The main program to run 
import tigers, bc_jail
 
players = tigers.get_players()
inmates = bc_jail.get_inmates()
 
for inmate in inmates:
    full_name = inmate['First Name'] + ' ' + inmate['Last Name']
 
    for player in players:
        # Swap commented condition to only match by last name.
        if player['Name'] == full_name:
        #if player['Name'].split(' ')[1] == inmate['Last Name']:
            print "Possible match found!"
            print "Player:"
            for key, value in player.items():
                print '    ' + key + ': ' + value
            print "Inmate:"
            for key, value in inmate.items():
                print '    ' + key + ': ' + value
            print ''
            break