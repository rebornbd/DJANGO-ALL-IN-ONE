### pure restapi with JWT

#### variations
```
01) function based view: FVB
02) class based view:    CBV
```

#### user type
```
general
admin
```

#### methods & permession
```
method  :   view    :   permession
----------------------------------
GET     |  LVIEW    |   G, A, unregister
POST    |  CVIEW    |   G, A
PUT     |  UVIEW    |   G, A
DELETE  |  DVIEW    |   A

NB:
LVIEW = List View
CVIEW = Create View
UVIEW = Update View
DVIEW = Delete View

G = General User
A = Admin User
```

### the end
