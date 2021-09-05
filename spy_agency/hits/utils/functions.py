from accounts.models import Boss, Hitman


def is_boss(user):
    """
        Know if user type boss
        Args:
            user : user logged
            type : django.utils.functional.SimpleLazyObject'
        
        Returns: bool
    """
    try:
        boss = Boss.objects.get(user=user)
        if boss:
            return True
    except Boss.DoesNotExist:
        return False
    
    except:
        return False



def get_hitmen(user):
    """
        Get hitmen by user(Boss, SuperUser)
        Args:
            user : user logged
            type : django.utils.functional.SimpleLazyObject'
        
        Returns: QuerySet []
    """
    try:
        hitmen = Hitman.objects.all()

        if is_boss(user):            
            boss = Boss.objects.get(user=user)
            hitmen = Hitman.objects.filter(boss=boss)
    except:
        return Hitman.objects.none()
    
    finally:
        return hitmen