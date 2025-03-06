Type: Handicap, compact, large, motorcycle
Monitoring system

Objects:
    Parking lot system
                    -- singleton design pattern
                    all other object is follows factory design pattern
    Entry/Exit terminals
        Printers
        Payment processor
    Parking spot
    Ticket
    Database
    Monitoring system


    Parking spot 
        have enum for the vehicle type:
            large
            medium
            small
            handicaped
            Motorcycle
            Ev charge
        
    Parking spot class:


    Parking spot class have derived class:
        handicaped parking spot
        large vehicle parking spot
        small vehicle parking spot
        Motorcycle parking spot


    Ticket class:
        id
        paking spot id
        parking spot type
        issue time

    Terminal class:
        get id
    Terminal class have derived class:
        Entry terminal:
            ticket = getTicket(parking spot)
        Exit terminal:
            except the ticket(ticket)

    ParkingAssignmentStratagy:
        getParkingSpot(terminal)
        releaseParkingspot(parking spot)

        derived:
            parking spot near entrance stratagy

    PaymentProcessor:

        derived:
            Creditcard payment processing
            Cash payment processing
    
    Tarif calculator
        calculate tarif(time, parking spot type)

        derived:
            weekday tarif calculator
            weekend tarif calculator
            pick hour tarif calculator


    Parking lot system
                    -- singleton design pattern
                    all other object is follows factory design pattern
        ticket = getparkingspot(terminal)
        

