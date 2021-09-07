from accounts.models import Boss, Hitman, State
from hits.models import Hit
from django.shortcuts import render

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

    except Exception as err:
        return False
    except Boss.DoesNotExist as err:
        return False    
    except:
        return False

def is_hitman(user):
    """
        Know if user type hitman
        Args:
            user : user logged
            type : django.utils.functional.SimpleLazyObject'
        
        Returns: bool
    """
    try:
        hitman = Hitman.objects.get(user=user)
        if hitman:
            return True
    
    except Exception as err:
        return False
    except Hitman.DoesNotExist as err:
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
    except Exception as err:
        return []
    except Boss.DoesNotExist as err:
        return []
    finally:
        return hitmen

def get_hits(user):
    """
        Get hits by user(Boss, SuperUser, Hitman)
        Args:
            user : user logged
            type : django.utils.functional.SimpleLazyObject'
        
        Returns: QuerySet []
    """
    try:
        
        hits = Hit.objects.all()

        if is_boss(user):
            hits = Hit.objects.filter(hitman__boss__user=user)
        elif is_hitman(user):
            hits = Hit.objects.filter(hitman__user=user)

    except Exception as err:    
        return []
    except Hit.DoesNotExist as err:
        return []
    except Boss.DoesNotExist as err:
        return []
    finally:
        return hits